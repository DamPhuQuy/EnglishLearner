namespace :notebook do
  desc "Display database statistics and metrics"
  task stats: :environment do
    puts "=== IELTS Database Administration Stats ==="
    puts "Environment: #{Rails.env}"
    puts "Database Adapter: #{ActiveRecord::Base.connection.adapter_name}"
    puts "Total Notebooks: #{Notebook.count}"
    puts "Total Cells: #{Cell.count}"
    puts "Cells by Skill Type:"
    Cell.group(:cell_type).count.each do |skill, count|
      puts "  - #{skill}: #{count}"
    end
    puts "Total Snapshots: #{NotebookSnapshot.count}"

    db_path = ActiveRecord::Base.connection_db_config.database
    if File.exist?(db_path)
      size_kb = (File.size(db_path) / 1024.0).round(2)
      puts "Database file: #{db_path} (#{size_kb} KB)"
    end
  end

  desc "Backup all notebooks and cells to a JSON file"
  task backup: :environment do
    backup_dir = Rails.root.join("storage", "backups")
    FileUtils.mkdir_p(backup_dir)

    timestamp = Time.current.strftime("%Y%m%d_%H%M%S")
    file_path = backup_dir.join("notebooks_backup_#{timestamp}.json")

    data = {
      backup_timestamp: Time.current.iso8601,
      notebooks_count: Notebook.count,
      notebooks: Notebook.all.map(&:as_json)
    }

    File.write(file_path, JSON.pretty_generate(data))
    puts "Backup successfully created: #{file_path} (#{data[:notebooks_count]} notebooks)"
  end

  desc "Restore notebooks from a JSON backup file"
  task :restore, [:file_path] => :environment do |_, args|
    file_path = args[:file_path]
    abort "Usage: bin/rake notebook:restore[path/to/backup.json]" if file_path.blank?
    abort "File not found: #{file_path}" unless File.exist?(file_path)

    raw = File.read(file_path)
    data = JSON.parse(raw)
    notebooks = data["notebooks"] || [data]

    ActiveRecord::Base.transaction do
      notebooks.each do |nb_data|
        id = nb_data["id"]
        title = nb_data["title"]
        cells = nb_data["cells"] || []

        nb = Notebook.find_or_initialize_by(id: id)
        nb.title = title
        nb.save!
        nb.sync_cells!(cells, reason: "rake_restore")
        puts "Restored notebook #{id} (#{title}) with #{cells.size} cells."
      end
    end

    puts "Restore completed successfully."
  end

  desc "Prune old snapshots across all notebooks"
  task :prune_snapshots, [:keep] => :environment do |_, args|
    keep = (args[:keep] || 25).to_i
    Notebook.pluck(:id).each do |nid|
      NotebookSnapshot.prune_for(nid, keep: keep)
    end
    puts "Snapshots pruned to maximum #{keep} per notebook."
  end
end
