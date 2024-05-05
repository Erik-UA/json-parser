from .action import Action

class ActionMeeting(Action):

    def write_headers(self) -> dict:
        fieldnames = [
            "engagement_createdAt",
            "engagement_lastUpdated",
            "engagement_type",
            "engagement_timestamp",
            # "engagement_source",
            # "engagement_bodyPreview",
            # "metadata_subject",
            # "metadata_text",
            # "metadata_from_email",
            # "metadata_from_firstName",
            # "metadata_from_lastName",
            # "metadata_to_0_email",
            # "metadata_to_0_firstName",
            # "metadata_to_0_lastName",
            # "metadata_sender_email"
        ]
        return fieldnames

    def parse_action(self, data: dict):

        for i in data:
            if i.get("engagement", {}).get("type") in ["MEETING"]:
                row_data = {
                    "engagement_createdAt": i["engagement"]["createdAt"],
                    "engagement_lastUpdated": i["engagement"]["lastUpdated"],
                    "engagement_type": i["engagement"]["type"],
                    "engagement_timestamp": i["engagement"]["timestamp"],

                    # "metadata_subject": i["metadata"]["subject"],
                    # "metadata_text": i["metadata"]["text"],
                    # "metadata_from_email": i["metadata"]["from"]["email"],
                    # "metadata_from_firstName": i["metadata"]["from"].get("firstName", ""),
                    # "metadata_from_lastName": i["metadata"]["from"].get("lastName", ""),
                    # "metadata_to_0_email": i["metadata"]["to"][0]["email"],
                    # "metadata_to_0_firstName": i["metadata"]["to"][0].get("firstName", ""),
                    # "metadata_to_0_lastName": i["metadata"]["to"][0].get("lastName", ""),
                    # "metadata_sender_email": i["metadata"]["sender"]["email"]
                }
                self.writer.writerow(row_data)