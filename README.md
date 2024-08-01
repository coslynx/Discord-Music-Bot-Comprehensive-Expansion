<h1 align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
  <br>Discord-Music-Bot-Comprehensive-Expansion
</h1>
<h3>◦ A powerful Discord bot built with Python and discord.py for playing music from YouTube, Spotify, and SoundCloud.</h3>
<h3>◦ Developed with the software and tools below.</h3>
<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue" alt="">
  <img src="https://img.shields.io/badge/Framework-discord.py-red" alt="">
  <img src="https://img.shields.io/badge/Database-Redis%20(Optional)-blue" alt="">
  <img src="https://img.shields.io/badge/APIs-Discord%2C%20YouTube%2C%20Spotify%2C%20SoundCloud-black" alt="">
</p>
<p align="center">
  <img src="https://img.shields.io/github/license/spectra-ai-codegen/Discord-Music-Bot-Comprehensive-Expansion?style=flat-square&color=5D6D7E" alt="GitHub license" />
  <img src="https://img.shields.io/github/last-commit/spectra-ai-codegen/Discord-Music-Bot-Comprehensive-Expansion?style=flat-square&color=5D6D7E" alt="git-last-commit" />
  <img src="https://img.shields.io/github/commit-activity/m/spectra-ai-codegen/Discord-Music-Bot-Comprehensive-Expansion?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
  <img src="https://img.shields.io/github/languages/top/spectra-ai-codegen/Discord-Music-Bot-Comprehensive-Expansion?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</p>

## 📑 Table of Contents
- [📍 Overview](#overview)
- [📦 Features](#features)
- [📂 Repository Structure](#repository-structure)
- [💻 Installation](#installation)
- [🏗️ Usage](#usage)
- [🌐 Hosting](#hosting)
- [📄 License](#license)
- [👏 Authors and Acknowledgments](#authors-and-acknowledgments)

## 📍 Overview
This repository houses a comprehensive Discord music bot project, designed to deliver an engaging and user-friendly music experience within Discord voice channels. The bot leverages a robust Python framework and integrates with popular streaming services like YouTube, Spotify, and SoundCloud, allowing users to play music, manage queues, and customize their listening experience.

## 📦 Features
- **Music Playback:** 
    - Play music from YouTube, Spotify, and SoundCloud.
    - Manage a music queue, adding, removing, and skipping tracks.
    - Control playback: play, pause, resume, stop.
    - Adjust playback volume.
    - Loop individual songs or the entire queue.
- **User Interface:**
    - Simple and intuitive command system for user interaction.
    - Display current song information, queue status, and relevant details.
    - Rich messages using Discord embeds for a visually appealing experience.
    - Customizable features like command aliases.
- **Voice Channel Integration:**
    - Seamlessly join and leave voice channels based on commands.
    - Automatic disconnection after inactivity or queue completion.
    - Handle voice channel permissions and restrictions.
- **Additional Features:**
    - Custom playlists for users to create and manage their favorite music.
    - Radio mode for listening to live radio streams.
    - Music recommendations based on user preferences (optional).
    - User-defined permissions for controlling bot access and functionality.
    - Integration with other Discord features like custom emojis or reactions.
- **Scalability and Maintenance:**
    - Scalable design for handling large numbers of users and servers.
    - Robust server infrastructure for optimal performance.
    - Regular maintenance for stability, security, and functionality.
    - Bug fixing, library updates, and security patches.

## 📂 Repository Structure

```
└── ./
    └── cogs: This directory contains cogs, which are essentially modules or extensions for the Discord bot. Each cog encapsulates a specific set of functionalities. 
        └── music.py: This file is responsible for all music-related commands and logic, including search, playback, queue management, and related functionalities. It relies on the `utils` directory for functionalities such as audio processing, API interaction, and playlist management. It also interacts with the main bot file `main.py` for command registration and integration.

    └── utils:  This directory contains utility modules and classes that provide reusable functionalities for the Discord bot.
        └── music_player.py: This file implements the `MusicPlayer` class, responsible for managing music playback, handling audio processing, and controlling the music queue. This file is used by the `music.py` cog to play music and manage the music queue. It might also interact with other utility files for specific tasks. 

```

## 💻 Installation
### 🔧 Prerequisites
- Python 3.7 or later
- pip

### 🚀 Setup Instructions
1. **Clone the repository:**
   - `git clone https://github.com/spectra-ai-codegen/Discord-Music-Bot-Comprehensive-Expansion.git`
2. **Navigate to the project directory:**
   - `cd Discord-Music-Bot-Comprehensive-Expansion`
3. **Install dependencies:**
   - `pip install -r requirements.txt`
4. **Create a `.env` file:**
   - Create a file named `.env` in the root directory and add the following environment variables:
     ```
     DISCORD_TOKEN=<your_discord_bot_token>
     ```
     Replace `<your_discord_bot_token>` with your actual Discord bot token.
5. **Run the bot:**
   - `python main.py`

## 🏗️ Usage
### 🤖 Bot Commands
- **`!play [song name/URL]`:** Play a song from YouTube, Spotify, or SoundCloud.
- **`!join`:** Join the user's voice channel.
- **`!leave`:** Leave the current voice channel.
- **`!queue`:** Display the current music queue.
- **`!skip`:** Skip to the next song in the queue.
- **`!stop`:** Stop music playback.
- **`!pause`:** Pause music playback.
- **`!resume`:** Resume music playback.
- **`!loop`:** Toggle song looping.
- **`!queue_loop`:** Toggle queue looping.
- **`!volume [volume level]`:** Set the playback volume.

## 🌐 Hosting
### 🚀 Deployment Instructions
1. **Create a Heroku account:** [https://www.heroku.com/](https://www.heroku.com/)
2. **Install the Heroku CLI:** [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)
3. **Login to Heroku:**
   - `heroku login`
4. **Create a new Heroku app:**
   - `heroku create <your_app_name>` (Replace `<your_app_name>` with your desired app name)
5. **Configure Heroku settings:**
   - Set the `DISCORD_TOKEN` environment variable in your Heroku app settings.
6. **Deploy the bot:**
   - `git push heroku main`

## 📄 License
This project is licensed under the GNU AGPLv3.

## 👥 Authors and Acknowledgments
- **Author Name** - [Spectra.codes](https://spectra.codes)
- **Creator Name** - [DRIX10](https://github.com/Drix10)

  (THE PART BELOW REMAINS SAME IN ALL THE README.md files, DO NOT CHANGE ANYTHING BELOW and DO not include this line)

  <p align="center">
    <h1 align="center">🌐 Spectra.Codes</h1>
  </p>
  <p align="center">
    <em>Why only generate Code? When you can generate the whole Repository!</em>
  </p>
  <p align="center">
	<img src="https://img.shields.io/badge/Developer-Drix10-red" alt="">
	<img src="https://img.shields.io/badge/Website-Spectra.codes-blue" alt="">
	<img src="https://img.shields.io/badge/Backed_by-Google_&_Microsoft_for_Startups-red" alt="">
	<img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4-black" alt="">
  <p>