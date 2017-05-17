class CreateComments < ActiveRecord::Migration[5.0]
  def change
    create_table :comments do |t|
      t.references :imageable, polymorphic: true

      t.timestamps
    end
  end
end
