module Api
  module V1
    class HealthController < ApplicationController
      def index
        db_connected = begin
          ActiveRecord::Base.connection.execute("SELECT 1")
          true
        rescue StandardError
          false
        end

        notebooks_count = Notebook.count
        cells_count = Cell.count
        snapshots_count = NotebookSnapshot.count

        render json: {
          status: "ok",
          database: db_connected ? "connected" : "disconnected",
          adapter: ActiveRecord::Base.connection.adapter_name,
          environment: Rails.env,
          notebooksCount: notebooks_count,
          cellsCount: cells_count,
          snapshotsCount: snapshots_count,
          timestamp: Time.current.iso8601
        }
      rescue StandardError => e
        render json: {
          status: "error",
          database: "error",
          message: e.message
        }, status: :service_unavailable
      end
    end
  end
end
