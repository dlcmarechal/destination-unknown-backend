require 'open3'
require 'json'

class HolidayDestinationController < ApplicationController
  def generate
    stdout, _ = Open3.capture2("python holiday-destination/output-suggestions.py " << JSON.generate(request.body.read))
    render json: {"country" => stdout.chomp }
  end
end
