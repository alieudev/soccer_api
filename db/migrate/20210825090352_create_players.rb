class CreatePlayers < ActiveRecord::Migration[6.1]
  def change
    create_table :players do |t|
      t.string :name
      t.integer :height
      t.integer :weight
      t.string :foot
      t.integer :rating
      t.string :image
      t.date :dob
      t.string :country
      t.integer :number
      t.belongs_to :team, foreign_key: true
    end
  end
end
