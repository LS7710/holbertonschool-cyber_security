elsif options[:list]
  tasks = File.readlines(TASK_FILE, chomp: true)
  if tasks.empty?
    puts "No tasks found."
  else
    puts "Tasks:"
    tasks.each_with_index { |task, i| puts "#{i + 1}. #{task}" }
  end
