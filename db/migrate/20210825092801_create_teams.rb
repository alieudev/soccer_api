class CreateTeams < ActiveRecord::Migration[6.1]
  def change
    create_table :teams do |t|
      t.string :name
      t.string :crest_url
      t.string :club_colors
      t.string :venue
      t.integer :founded
    end
  end
end