class NotebookSnapshot < ApplicationRecord
  belongs_to :notebook

  validates :snapshot_data, presence: true

  def doc
    JSON.parse(snapshot_data)
  rescue JSON::ParserError
    {}
  end

  def self.prune_for(notebook_id, keep: 25)
    total = where(notebook_id: notebook_id).count
    if total > keep
      excess_ids = where(notebook_id: notebook_id)
                     .order(created_at: :desc)
                     .offset(keep)
                     .pluck(:id)
      where(id: excess_ids).delete_all if excess_ids.any?
    end
  end

  def summary_json
    {
      id: id,
      notebookId: notebook_id,
      title: title,
      cellsCount: cells_count,
      reason: reason,
      createdAt: created_at&.iso8601
    }
  end
end
