from pinecone import Pinecone
pc = Pinecone(api_key="pcsk_3HXpb7_CeLmGai1mJE1f3opWsj6v3teu91frpJa1pckD6pUKKgRFsBe9md39VGsNfm2ghm")

assistant = pc.assistant.Assistant(
    assistant_name="sol-seekers", 
)

response = assistant.upload_file(
    file_path="student_discipline_guidelines.pdf",
    timeout=None
)