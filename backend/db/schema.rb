# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[8.1].define(version: 2026_10_25_160000) do
  create_table "cells", id: :string, force: :cascade do |t|
    t.string "notebook_id", null: false
    t.integer "position", default: 0, null: false
    t.string "cell_type", default: "markdown", null: false
    t.integer "execution_count"
    t.text "source", default: ""
    t.string "resource_type", default: "none"
    t.text "resource_url"
    t.string "resource_name"
    t.text "resource_text_content"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["cell_type"], name: "index_cells_on_cell_type"
    t.index ["notebook_id", "position"], name: "index_cells_on_notebook_id_and_position"
  end

  create_table "notebook_snapshots", force: :cascade do |t|
    t.string "notebook_id", null: false
    t.string "title", null: false
    t.text "snapshot_data", null: false
    t.integer "cells_count", default: 0, null: false
    t.string "reason", default: "auto_sync"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["notebook_id", "created_at"], name: "index_notebook_snapshots_on_notebook_id_and_created_at"
  end

  create_table "notebooks", id: :string, force: :cascade do |t|
    t.string "title", default: "IELTS Practice Notebook", null: false
    t.text "description"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  add_foreign_key "cells", "notebooks", on_delete: :cascade
  add_foreign_key "notebook_snapshots", "notebooks", on_delete: :cascade
end
