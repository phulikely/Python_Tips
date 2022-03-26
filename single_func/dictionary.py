#32 Use items() to directly unpack dictionary values
teams_by_color = {"blue": ["Patrick", "Jessi", "Harp"], "red": ["Hans", "POP"]}
for team_color, players in teams_by_color.items():
	if 'ue' in team_color:
		print(players)

