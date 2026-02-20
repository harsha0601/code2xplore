platform = input("Choose your music platform (Prime Music / Spotify / Apple Music): ")
if platform.lower() in ["prime music", "spotify", "apple music"]:
    print("\nPlatform:", platform.title())
else:
    print("Enter correct platform")
    exit()
data = input("Enter song durations separated by space: ")
parts = data.split()
playlist = [0] * len(parts)
for i in range(len(parts)):
    playlist[i] = int(parts[i])
invalid = False
for duration in playlist:
    if duration <= 0:
        invalid = True
        break
if invalid:
    print("\nInvalid Playlist: Durations must be greater than 0")
else:
    total_duration = sum(playlist)
    number_of_songs = len(playlist)
    repetitive = False
    for x in playlist:
        if playlist.count(x) > 1:
            repetitive = True
            break
    if total_duration < 300:
        category = "Too Short Playlist"
        recommendation = "Add more songs for a better experience"
    elif total_duration > 3600:
        category = "Too Long Playlist"
        recommendation = "Consider reducing playlist length"
    elif repetitive:
        category = "Repetitive Playlist"
        recommendation = "Add variety"
    elif 300<total_duration<3600:
        category = "Balanced Playlist"
        recommendation = "Good listening session"
    else:
        category = "Irregular Playlist"
        recommendation = "Modify playlist for better balance"
    print("\nTotal Duration:", total_duration, "seconds")
    print("Songs:", number_of_songs)
    print("Category:", category, "in", platform)
    print("Recommendation:", recommendation)