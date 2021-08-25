class ApplicationController < Sinatra::Base
  set :default_content_type, 'application/json'
  
  # Add your routes here
  get "/" do
    { message: "Good luck with your project!" }.to_json
  end

  get '/players' do
    Player.all.to_json
  end

  delete '/players/:id' do
    player = Player.find(params[:id])
    player.destroy
    player.to_json
  end

  post '/players' do
    player = Player.create(
      name: params[:name],
      height: params[:height],
      weight: params[:weight],
      foot: params[:foot],
      rating: params[:rating],
      team_id: params[:team_id]
    )
    player.to_json
  end

  patch '/players/:id' do
    player = Player.update(
      name: params[:name],
      height: params[:height],
      weight: params[:weight],
      foot: params[:foot],
      rating: params[:rating],
    )
    player.to_json
  end
end