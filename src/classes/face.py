from pathlib import Path

import cv2


class FaceDetector:
    def __init__(self, path: str | None = None) -> None:
        """
        Initialize the FaceDetector class
        """
        self.classifier = cv2.CascadeClassifier(
            path if path else "data/haarcascade_frontalface_alt.xml"
        )

    def detect_video(self, input_path: Path, output_path: Path) -> None:
        """
        Detect faces in a video file
        """
        if not input_path.exists():
            raise FileNotFoundError(f"{input_path} does not exist")

        if output_path.exists():
            raise FileExistsError(f"{output_path} already exists")

        video_cap = cv2.VideoCapture(str(input_path.absolute()))

        video_writer = cv2.VideoWriter(
            filename=str(output_path),
            fourcc=cv2.VideoWriter_fourcc(*"mp4v"),  # type: ignore
            fps=video_cap.get(cv2.CAP_PROP_FPS),
            frameSize=(
                int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
            ),
        )

        while video_cap.isOpened():
            ret, video_data = video_cap.read()

            if not ret:
                break

            gray = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

            faces = self.classifier.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE,
            )

            for x, y, w, h in faces:
                cv2.rectangle(
                    img=video_data,
                    pt1=(x, y),
                    pt2=(x + w, y + h),
                    color=(255, 0, 0),
                    thickness=2,
                )

            video_writer.write(video_data)

        video_cap.release()
        video_writer.release()
        cv2.destroyAllWindows()
