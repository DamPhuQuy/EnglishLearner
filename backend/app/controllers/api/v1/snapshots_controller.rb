module Api
  module V1
    class SnapshotsController < ApplicationController
      before_action :set_notebook

      # GET /api/v1/notebooks/:notebook_id/snapshots
      def index
        snapshots = @notebook.snapshots.order(created_at: :desc).map(&:summary_json)
        render json: { snapshots: snapshots }
      end

      # GET /api/v1/notebooks/:notebook_id/snapshots/:id
      def show
        snapshot = @notebook.snapshots.find(params[:id])
        render json: {
          snapshot: snapshot.summary_json,
          doc: snapshot.doc
        }
      end

      # POST /api/v1/notebooks/:notebook_id/snapshots/:id/restore
      def restore
        snapshot = @notebook.snapshots.find(params[:id])
        @notebook.restore_from_snapshot!(snapshot)
        render json: {
          message: "Notebook successfully restored from snapshot #{snapshot.id}",
          notebook: @notebook.as_json
        }
      end

      private

      def set_notebook
        @notebook = Notebook.find(params[:notebook_id])
      end
    end
  end
end
