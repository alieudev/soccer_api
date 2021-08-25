require 'json'
file = File.read('leicester_city.json')
leicester_city = JSON.parse(file)

leicester_city.each do |player|
    puts player["Name"]
end