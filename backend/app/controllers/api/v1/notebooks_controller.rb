module Api
  module V1
    class NotebooksController < ApplicationController
      before_action :set_notebook, only: [:show, :update, :destroy, :sync, :export]

      # GET /api/v1/notebooks
      def index
        notebooks = Notebook.order(updated_at: :desc).map(&:summary_json)
        render json: { notebooks: notebooks }
      end

      # GET /api/v1/notebooks/current
      def current
        notebook = Notebook.order(updated_at: :desc).first || Notebook.default_notebook
        render json: notebook.as_json
      end

      # GET /api/v1/notebooks/:id
      def show
        render json: @notebook.as_json
      end

      # POST /api/v1/notebooks
      def create
        notebook = Notebook.new(notebook_params)
        notebook.id = params[:id] if params[:id].present?

        if notebook.save
          if params.key?(:cells)
            notebook.sync_cells!(extract_cells_param, reason: "create")
          end
          render json: notebook.as_json, status: :created
        else
          render json: { errors: notebook.errors.full_messages }, status: :unprocessable_entity
        end
      end

      # PUT/PATCH /api/v1/notebooks/:id
      def update
        if @notebook.update(notebook_params)
          render json: @notebook.as_json
        else
          render json: { errors: @notebook.errors.full_messages }, status: :unprocessable_entity
        end
      end

      # PUT /api/v1/notebooks/:id/sync
      def sync
        if params[:title].present? && params[:title] != @notebook.title
          @notebook.update(title: params[:title])
        end

        if params.key?(:cells)
          reason = params[:reason] || "auto_sync"
          @notebook.sync_cells!(extract_cells_param, reason: reason)
        end

        render json: @notebook.as_json
      rescue StandardError => e
        render json: { error: e.message }, status: :unprocessable_entity
      end

      # DELETE /api/v1/notebooks/:id
      def destroy
        @notebook.destroy
        head :no_content
      end

      # GET /api/v1/notebooks/:id/export
      def export
        filename = "#{@notebook.title.parameterize.presence || 'notebook'}.ilnb"
        send_data(
          JSON.pretty_generate(@notebook.as_json),
          type: "application/json; charset=utf-8",
          disposition: "attachment; filename=\"#{filename}\""
        )
      end

      # POST /api/v1/notebooks/import
      def import
        doc = params.require(:notebook).permit!.to_h

        id = doc["id"].presence || doc[:id].presence || SecureRandom.uuid
        title = doc["title"].presence || doc[:title].presence || "Imported Notebook"
        cells = doc["cells"] || doc[:cells] || []

        notebook = Notebook.find_or_initialize_by(id: id)
        notebook.title = title
        notebook.save!
        notebook.sync_cells!(cells, reason: "import")

        render json: notebook.as_json, status: :created
      rescue StandardError => e
        render json: { error: e.message }, status: :unprocessable_entity
      end

      private

      def set_notebook
        if params[:id] == "current" || params[:id] == "default"
          @notebook = Notebook.order(updated_at: :desc).first || Notebook.default_notebook
        else
          @notebook = Notebook.find_by(id: params[:id])
          unless @notebook
            @notebook = Notebook.create!(id: params[:id], title: params[:title] || "IELTS Practice Notebook")
          end
        end
      end

      def notebook_params
        params.fetch(:notebook, {}).permit(:title, :description)
      end

      def extract_cells_param
        raw_cells = params[:cells]
        return [] unless raw_cells.is_a?(Array)

        raw_cells.map do |c|
          if c.respond_to?(:to_unsafe_h)
            c.to_unsafe_h
          elsif c.is_a?(Hash)
            c
          else
            {}
          end
        end
      end
    end
  end
end
