import cv2
import numpy as np
import av
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

RTC_CONFIGURATION = RTCConfiguration(
    {
      "RTCIceServer": [{
        "urls": ["turn:turn.xxx.dev:5349"],
        "username": "user",
        "credential": "password",
      }]
    }
)

class VideoProcessor:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_ctx = webrtc_streamer(
    key="WYH",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    video_processor_factory=VideoProcessor,
    async_processing=True,
)
