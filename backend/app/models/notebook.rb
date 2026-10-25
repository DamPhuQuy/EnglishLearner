class Notebook < ApplicationRecord
  has_many :cells, -> { order(position: :asc) }, dependent: :destroy, inverse_of: :notebook
  has_many :snapshots, -> { order(created_at: :desc) }, class_name: "NotebookSnapshot", dependent: :destroy

  validates :title, presence: true

  before_validation :ensure_id

  def self.default_notebook
    first_or_create!(
      id: "default-ielts-notebook",
      title: "IELTS Practice Notebook"
    )
  end

  def sync_cells!(cells_payload, reason: "sync")
    transaction do
      payload_list = cells_payload || []
      incoming_ids = payload_list.map { |c| (c[:id] || c["id"]).to_s }.compact

      # Remove cells not in incoming payload
      cells.where.not(id: incoming_ids).destroy_all

      payload_list.each_with_index do |cell_data, idx|
        c_hash = cell_data.respond_to?(:to_h) ? cell_data.to_h.with_indifferent_access : cell_data
        cid = c_hash[:id].to_s.presence || SecureRandom.uuid

        cell = cells.find_or_initialize_by(id: cid)
        cell.position = idx
        cell.cell_type = c_hash[:cellType] || c_hash[:cell_type] || "markdown"
        cell.execution_count = c_hash[:executionCount] || c_hash[:execution_count]
        cell.source = c_hash[:source] || ""
        cell.resource = c_hash[:resource]
        cell.save!
      end

      touch

      # Create snapshot for database safety and disaster recovery
      record_snapshot!(reason: reason)
    end

    reload
  end

  def record_snapshot!(reason: "manual")
    # Avoid duplicate snapshots within 30 seconds unless explicitly requested
    latest = snapshots.first
    if latest && latest.created_at > 30.seconds.ago && reason == "auto_sync"
      return latest
    end

    snap = snapshots.create!(
      title: title,
      snapshot_data: as_json.to_json,
      cells_count: cells.count,
      reason: reason
    )
    NotebookSnapshot.prune_for(id, keep: 25)
    snap
  end

  def restore_from_snapshot!(snapshot)
    transaction do
      data = snapshot.doc
      self.title = data["title"] if data["title"].present?
      save!
      sync_cells!(data["cells"], reason: "restore_from_snapshot_#{snapshot.id}")
    end
    reload
  end

  def as_json(options = nil)
    {
      id: id,
      title: title,
      cells: cells.map(&:as_json),
      createdAt: created_at&.iso8601,
      updatedAt: updated_at&.iso8601
    }
  end

  def summary_json
    {
      id: id,
      title: title,
      cellsCount: cells.count,
      createdAt: created_at&.iso8601,
      updatedAt: updated_at&.iso8601
    }
  end

  private

  def ensure_id
    self.id = SecureRandom.uuid if id.blank?
  end
end
