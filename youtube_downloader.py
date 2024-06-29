import customtkinter as ctk
from pytube import YouTube
from tkinter import filedialog
import os
import threading

class YouTubeDownloader:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("YouTube Downloader")
        self.window.geometry("800x600")
        
        self.create_widgets()

    def create_widgets(self):
        # URL input
        self.url_label = ctk.CTkLabel(self.window, text="Enter YouTube URL:")
        self.url_label.pack(pady=10)
        self.url_entry = ctk.CTkEntry(self.window, width=500)
        self.url_entry.pack(pady=10)

        # Download button
        self.download_button = ctk.CTkButton(self.window, text="Download", command=self.start_download)
        self.download_button.pack(pady=20)

        # Status label
        self.status_label = ctk.CTkLabel(self.window, text="")
        self.status_label.pack(pady=10)

        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(self.window, width=400)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10)
        self.progress_bar.pack_forget()  # Hide initially

    def start_download(self):
        url = self.url_entry.get().strip()
        if not url:
            self.status_label.configure(text="Please enter a valid YouTube URL")
            return

        threading.Thread(target=self.download_video, args=(url,), daemon=True).start()

    def download_video(self, url):
        try:
            yt = YouTube(url, on_progress_callback=self.on_progress)
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

            if not stream:
                self.status_label.configure(text="No suitable video stream found")
                return

            default_path = os.path.join(os.path.expanduser("~"), "Downloads")
            save_path = filedialog.asksaveasfilename(
                initialdir=default_path,
                defaultextension=".mp4",
                filetypes=[("MP4 files", "*.mp4")],
                initialfile=f"{yt.title}.mp4"
            )

            if not save_path:
                self.status_label.configure(text="Download cancelled")
                return

            self.status_label.configure(text="Download in progress...")
            self.progress_bar.pack()

            stream.download(filename=save_path)

            self.status_label.configure(text="Download completed successfully!")
            self.progress_bar.set(0)
            self.progress_bar.pack_forget()
            
            # Clear the URL entry field after successful download
            self.window.after(0, self.clear_url_entry)

        except Exception as e:
            self.status_label.configure(text=f"Error: {str(e)}")
            self.progress_bar.pack_forget()

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        self.progress_bar.set(percentage / 100)
        self.window.update_idletasks()

    def clear_url_entry(self):
        self.url_entry.delete(0, 'end')

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Set the theme to dark mode
    ctk.set_default_color_theme("blue")
    app = YouTubeDownloader()
    app.run()