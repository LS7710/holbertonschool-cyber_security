#!/usr/bin/env ruby
require 'open-uri'
require 'uri'
require 'fileutils'

if ARGV.length != 2
  puts "Usage: #{__FILE__} URL LOCAL_FILE_PATH"
  exit
end

url = ARGV[0]
local_path = ARGV[1]

puts "Downloading file from #{url}..."

begin
  URI.open(url) do |remote_file|
    File.open(local_path, 'wb') do |file|
      file.write(remote_file.read)
    end
  end
  puts "File downloaded and saved to #{local_path}."
rescue => e
  puts "Failed to download file: #{e.message}"
end
