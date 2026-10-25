require "test_helper"

class Api::V1::NotebooksControllerTest < ActionDispatch::IntegrationTest
  setup do
    @notebook = Notebook.create!(
      id: "test-nb-1",
      title: "Test IELTS Notebook"
    )
    @notebook.sync_cells!([
      {
        id: "c1",
        cellType: "writing",
        source: "Essay intro",
        resource: { type: "text", name: "prompt.txt", textContent: "Prompt text" }
      },
      {
        id: "c2",
        cellType: "speaking",
        source: "Speaking notes"
      }
    ])
  end

  test "should list notebooks" do
    get api_v1_notebooks_url
    assert_response :success
    json = JSON.parse(response.body)
    assert json["notebooks"].any? { |n| n["id"] == "test-nb-1" }
  end

  test "should get notebook by id" do
    get api_v1_notebook_url(@notebook.id)
    assert_response :success
    json = JSON.parse(response.body)
    assert_equal "Test IELTS Notebook", json["title"]
    assert_equal 2, json["cells"].length
    assert_equal "Essay intro", json["cells"][0]["source"]
    assert_equal "text", json["cells"][0]["resource"]["type"]
  end

  test "should sync notebook title and cells atomically" do
    put sync_api_v1_notebook_url(@notebook.id), params: {
      title: "Updated Title",
      cells: [
        {
          id: "c1",
          cellType: "writing",
          source: "Updated Essay content"
        },
        {
          id: "c3-new",
          cellType: "listening",
          source: "New listening task",
          resource: { type: "audio", url: "https://example.com/audio.mp3" }
        }
      ]
    }, as: :json

    assert_response :success
    json = JSON.parse(response.body)
    assert_equal "Updated Title", json["title"]
    assert_equal 2, json["cells"].length

    # Verify in DB
    @notebook.reload
    assert_equal "Updated Title", @notebook.title
    assert_equal 2, @notebook.cells.count
    assert_equal ["c1", "c3-new"], @notebook.cells.pluck(:id)
    assert_equal "New listening task", @notebook.cells.find_by(id: "c3-new").source
  end

  test "should allow syncing empty cells list" do
    put sync_api_v1_notebook_url(@notebook.id), params: {
      title: "Empty Notebook",
      cells: []
    }, as: :json

    assert_response :success
    json = JSON.parse(response.body)
    assert_equal "Empty Notebook", json["title"]
    assert_equal 0, json["cells"].length

    @notebook.reload
    assert_equal 0, @notebook.cells.count
  end

  test "should get snapshots and restore" do
    get api_v1_notebook_snapshots_url(@notebook.id)
    assert_response :success
    json = JSON.parse(response.body)
    assert json["snapshots"].length >= 1
    snapshot_id = json["snapshots"].first["id"]

    # Now modify cells
    @notebook.sync_cells!([], reason: "empty_it")
    assert_equal 0, @notebook.cells.count

    # Now restore from snapshot
    post restore_api_v1_notebook_snapshot_url(@notebook.id, snapshot_id)
    assert_response :success
    @notebook.reload
    assert_equal 2, @notebook.cells.count
  end
end
