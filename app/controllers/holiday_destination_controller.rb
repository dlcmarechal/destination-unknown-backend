require 'open3'

class HolidayDestinationController < ApplicationController
  def generate
    stdout, _ = Open3.capture2("python holiday-destination/output-suggestions.py")
    render json: {"country" => stdout.chomp }
  end
end
