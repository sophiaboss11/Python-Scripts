import unreal, sys


# Get the Asset Registry
asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()

# Get all assets
all_assets =  actors = unreal.EditorLevelLibrary.get_all_level_actors()


# Function to select assets in the Content Browser
def select_assets_in_content_browser(assets):
    # print(assets[0].is_hidden_ed())
    assets[0].set_actor_hidden_in_game(False)
    # print(assets[0].is_hidden_ed())
    unreal.EditorLevelLibrary.set_selected_level_actors(assets)

# def select_inverse(assets):


# Find all hidden assets
hidden_assets = []
for asset in all_assets:
    # asset_data = asset.get_asset()f
    asset_data = asset
    # if asset_data and unreal.EditorAssetLibrary.is_asset_vible(asset_data) == False:
    if asset_data and unreal.Actor.is_hidden_ed(asset_data) == False:

        hidden_assets.append(asset)

# Select hidden assets in the Content Browser
# print(hidden_assets)
# test = all_assets[0], all_assets[1]


select_assets_in_content_browser(hidden_assets)
print(f"Selected {len(hidden_assets)} hidden assets in the Content Browser.")

