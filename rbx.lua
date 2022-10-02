local httpService = game:GetService("HttpService")

while true do
	
	data = string.upper(httpService:GetAsync('http://127.0.0.1:8080/get'))
	if tostring(data):find('NO CARD') then wait(0.01) continue end
	
	if tostring(data):find(game.ReplicatedStorage:WaitForChild("ValidKeycard").Value) then
		game.Workspace.KeycardDoor.Transparency = 1
		game.Workspace.KeycardDoor.CanCollide = false
		
		wait(3)
		game.Workspace.KeycardDoor.Transparency = 0
		game.Workspace.KeycardDoor.CanCollide = true
	end
	print(data)
	wait(0.01)
end
