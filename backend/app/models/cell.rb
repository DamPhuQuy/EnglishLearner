class Cell < ApplicationRecord
  VALID_CELL_TYPES = %w[listening reading writing speaking markdown].freeze

  belongs_to :notebook, inverse_of: :cells

  validates :cell_type, inclusion: { in: VALID_CELL_TYPES }
  validates :position, numericality: { greater_than_or_equal_to: 0 }

  before_validation :ensure_id

  def resource=(res)
    if res.is_a?(Hash) || (res.respond_to?(:to_h) && !res.nil?)
      h = res.to_h.with_indifferent_access
      self.resource_type = h[:type].presence || "none"
      self.resource_url = h[:url]
      self.resource_name = h[:name]
      self.resource_text_content = h[:textContent]
    else
      self.resource_type = "none"
      self.resource_url = nil
      self.resource_name = nil
      self.resource_text_content = nil
    end
  end

  def resource
    return nil if resource_type.blank? || resource_type == "none"

    data = { type: resource_type }
    data[:url] = resource_url if resource_url.present?
    data[:name] = resource_name if resource_name.present?
    data[:textContent] = resource_text_content if resource_text_content.present?
    data
  end

  def as_json(options = nil)
    res = resource
    data = {
      id: id,
      executionCount: execution_count,
      cellType: cell_type,
      source: source || ""
    }
    data[:resource] = res if res.present?
    data
  end

  private

  def ensure_id
    self.id = SecureRandom.uuid if id.blank?
  end
end
