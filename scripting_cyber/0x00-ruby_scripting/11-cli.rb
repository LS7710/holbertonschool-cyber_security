#!/usr/bin/env ruby
require 'optparse'

TASK_FILE = 'tasks.txt'

options = {}
OptionParser.new do |opts|
  opts.banner = "Usage: cli.rb [options]"

  opts.on("-a", "--add TASK", "Add a new task") do |task|
    options[:add] = task
  end

  opts.on("-l", "--list", "List all tasks") do
    options[:list] = true
  end

  opts.on("-r", "--remove INDEX", Integer, "Remove a task by index") do |index|
    options[:remove] = index
  end

  opts.on("-h", "--help", "Show help") do
    puts opts
    exit
  end
end.parse!

# Ensure the file exists
File.write(TASK_FILE, '') unless File.exist?(TASK_FILE)

if options[:add]
  File.open(TASK_FILE, 'a') { |f| f.puts(options[:add]) }
  puts "Task '#{options[:add]}' added."

elsif options[:list]
  tasks = File.readlines(TASK_FILE, chomp: true)
  if tasks.empty?
    puts "No tasks found."
  else
    tasks.each_with_index { |task, i| puts "#{i + 1}. #{task}" }
  end

elsif options[:remove]
  index = options[:remove] - 1
  tasks = File.readlines(TASK_FILE, chomp: true)

  if index < 0 || index >= tasks.size
    puts "Invalid index."
  else
    removed = tasks.delete_at(index)
    File.write(TASK_FILE, tasks.join("\n") + "\n")
    puts "Task '#{removed}' removed."
  end

else
  puts "Use -h for help"
end
