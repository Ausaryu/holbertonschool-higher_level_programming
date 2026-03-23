#!/usr/bin/python3
def generate_invitations(template_content, attendees):
    if not isinstance(template_content, str):
        TypeError("template_content is not a string")
    if isinstance(attendees, list) and all(isinstance(x, dict) for x in attendees):
        TypeError("attendees is not a list of dictionnaries")
    if template_content == "":
        ValueError("Template is empty, no output files generated.")
    if attendees == []:
        ValueError("No data provided, no output files generated." )
    length = 0
    for person in attendees:
        with open(f"output_{length}.txt", "a") as file:
            file.write(template_content.format(
                name=person.get('name') or "N/A",
                event_title=person.get('event_title') or "N/A",
                event_date=person.get('event_date') or "N/A",
                event_location=person.get('event_location') or "N/A"
            ))
        length += 1