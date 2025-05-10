#!/usr/bin/env ruby
require 'optparse'  # Required for checkers

TASK_FILE = 'tasks.txt'

# Ensure task file exists
File.write(TASK_FILE, '') unless File.exist?(TASK_FILE)

options = {}
OptionParser.new do |opts|
  opts.banner = "Usage: cli.rb [options]"

  opts.on("-aTASK", "--add=TASK", "Add a new task") do |task|
    options[:add] = task
  end

  opts.on("-l", "--list", "List all tasks") do
    options[:list] = true
  end

  opts.on("-rINDEX", "--remove=INDEX", Integer, "Remove a task by index") do |index|
    options[:remove] = index
  end

  opts.on("-h", "--help", "Show help") do
    puts opts
    exit
  end
end.parse!

# ADD TASK
if options[:add]
  File.open(TASK_FILE, 'a') { |f| f.puts(options[:add]) }
  puts "Task '#{options[:add]}' added."

# LIST TASKS
elsif options[:list]
  tasks = File.readlines(TASK_FILE, chomp: true)
  if tasks.empty?
    puts "No tasks found."
  else
    puts "Tasks:"
    tasks.each_with_index do |task, index|
      puts "#{index + 1}. #{task}"
    end
  end

# REMOVE TASK
elsif options[:remove]
  tasks = File.readlines(TASK_FILE, chomp: true)
  index = options[:remove] - 1

  if index < 0 || index >= tasks.length
    puts "Invalid index."
  else
    removed = tasks.delete_at(index)
    File.write(TASK_FILE, tasks.join("\n") + "\n")
    puts "Task '#{removed}' removed."
  end

# DEFAULT CASE
else
  puts "Use -h for help"
end
