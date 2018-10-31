require 'test_helper'

class HolidayDestinationControllerTest < ActionDispatch::IntegrationTest
  test "should get generate" do
    get holiday_destination_generate_url
    assert_response :success
  end

end
