# Automatic Population of Personal Knowledge Graphs from Streaming Platforms
<u style="text-decoration: none; -webkit-text-decoration-color: blue; text-decoration-color: blue;"></u>

The automatic population of a Personal Knowledge Graph based on personal data from streaming platforms is a solution that takes the user's personal data as input, processes it, carries out entity linking, and populates the user's PKG. Eirik Wilhelmsen and Ottar Jensen proposed The solution as part of a bachelor's project. The method is based on concepts such as PKG, Knowledge Bases (KBs), Entity Linking (EL), and Information Extraction (IE), all of which are examined and described in our thesis. The proposed solution is based on an already existing system called PKG-API, https://github.com/iai-group/pkg-api. The PKG API takes care of populating the PKG, while the method we have created stands for the content of what will populate the PKG.

The method's course of action consists of 3 steps respectively, illustrated in the figure below.
1. Extract personal data from services
2. Process the personal data
   1. Keep only the important bits of information (what the user likes, dislikes, etc)
   2. Entity link provided entities
        1. Search entities through KBs like Music Brainz and IMDb for corresponding entries
3. Convert data into a format acceptable for the PKG framework






Branch out to a premade demo branch and download requirements.txt to run the program correctly. Etter at PKG API'en provided by the IAI group is started in the background. Navigate to PKGs in the terminal and type Python app.py. From there, the index is opened on localhost 7000. 






Note that the Spotify API is unavailable unless a request is sent to Eirik with a Spotify email, and he adds you.



Contributors:
Eirik Wilhelmsen created EntityLinking.html, netflix.html, spotify.html, GroundTruthNetflix.py, GroundTruthSpotify.py, NetflixClass.py, PKGClass.py, SpotifyClass.py
Ottar Jensen created applemusic.html, AppleMusic.py, GroundTruthAppleM.txt, SystemOutputAppleM.txt

Worked together on:
app.py, Statements.py, index.html

