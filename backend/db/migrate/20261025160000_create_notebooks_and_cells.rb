class CreateNotebooksAndCells < ActiveRecord::Migration[8.1]
  def change
    create_table :notebooks, id: :string do |t|
      t.string :title, null: false, default: "IELTS Practice Notebook"
      t.text :description
      t.timestamps
    end

    create_table :cells, id: :string do |t|
      t.string :notebook_id, null: false
      t.integer :position, null: false, default: 0
      t.string :cell_type, null: false, default: "markdown"
      t.integer :execution_count
      t.text :source, default: ""
      t.string :resource_type, default: "none"
      t.text :resource_url
      t.string :resource_name
      t.text :resource_text_content
      t.timestamps
    end

    add_foreign_key :cells, :notebooks, column: :notebook_id, primary_key: :id, on_delete: :cascade
    add_index :cells, [:notebook_id, :position]
    add_index :cells, :cell_type

    create_table :notebook_snapshots do |t|
      t.string :notebook_id, null: false
      t.string :title, null: false
      t.text :snapshot_data, null: false
      t.integer :cells_count, null: false, default: 0
      t.string :reason, default: "auto_sync"
      t.timestamps
    end

    add_foreign_key :notebook_snapshots, :notebooks, column: :notebook_id, primary_key: :id, on_delete: :cascade
    add_index :notebook_snapshots, [:notebook_id, :created_at]
  end
end
