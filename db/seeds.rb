require 'json'
file = File.read('leicester_city.json')
leicester_city = JSON.parse(file)

puts "Deleting old stuff..."
    Player.destroy_all
    Team.destroy_all


puts "🌱 Seeding teams..."

        Team.create(
            name: Faker::Sports::Football.team,
            venue: Faker::WorldCup.stadium,
            founded: rand(1940..2000),
            club_colors: "#{Faker::Color.color_name}, #{Faker::Color.color_name}"
        )
    
puts "🌱 Seeding players..."
    leicester_city.each do |player|
        Player.create(
            name: player["Name"],
            weight: rand(150..200),
            height: rand(160..220),
            foot: ['left', 'right'].sample,
            rating: rand(50..100),
            team_id: Team.first.id,
            image: player["Image"],
            dob: player["DOB"],
            country: player["Country"],
            number: player["Number"],
        )
    end

puts "✅ Done seeding!"