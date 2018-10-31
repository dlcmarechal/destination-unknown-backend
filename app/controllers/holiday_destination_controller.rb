require 'open3'

class HolidayDestinationController < ApplicationController
  def generate
    stdout, _ = Open3.capture2("python output-suggestions.py")
    render json: stdout
  end
end
