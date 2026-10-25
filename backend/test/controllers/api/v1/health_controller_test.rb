require "test_helper"

class Api::V1::HealthControllerTest < ActionDispatch::IntegrationTest
  test "should get health status" do
    get api_v1_health_url
    assert_response :success
    json = JSON.parse(response.body)
    assert_equal "ok", json["status"]
    assert_equal "connected", json["database"]
    assert json.key?("notebooksCount")
    assert json.key?("cellsCount")
  end
end
