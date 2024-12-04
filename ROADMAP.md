# Roadmap

The full span of functionality that Dragonroost will eventually encompass.

## Currently available

Here are the things already available in Dragonroost

- **Animals**, which have the following features:
  - Physical characteristics like weight, age, color, sex, species.
  - Other attributes, including name, description, donation fee, status, a photo, and intake date.
  - Location of the animal in the rescue.
- **Medical Records**, which have the following features:
  - Each animal can have any number of medical records
  - Records allow to tracking weights, bowel movements, notes, and treatments.
  - The most recent record's weight will display on the Animal's page for their current weight.
- **Species**, which have the following features:
  - Name, description, diet, class (reptile, mammal, etc).
- **Locations**: with a description and a name. These can be physical buildings, areas in a single building, or any other variation.
- **Meetings**: For tracking periodic organizational meetings. Expects a link to a URL (for example,a Google Doc) but a file can be attached as well.
- **Medical Updates**: Different from medical records, these allow medical staff to upload notes or updates from their shift.
- **People**: Allows for tracking donors, fosters, volunteers, and vet staff and their personal information.

## Upcoming/Likely features

- [ ] **Animals module**:
  - [ ] Enhanced PDF export. PDF export exists for animal records, but the output is ugly.
  - [ ] Import from CSV.
- [ ] **Business module**:
  - [ ] Transactions (income/expenses).
  - [ ] *(Possible)* A light inventory tracking system.
- [ ] **Medical module**:
  - [ ] *(Possible)* Tracking of treatments or medications.
  - [ ] Vaccine calendar.
- [ ] **People module**: Integration of People into other aspects of Dragonroost - for example, tracking who attends Meetings, which animals are with which Fosters, and more

## Ongoing work

- [ ] **Frontend styling**: I find frontend UI/UX work to be the most difficult, and so the UI is going to be constantly upgraded over time as I get more comfortable with these skills. I plan to move from Bootstrap 5 to something like Tailwind eventually, but for now, the focus is on building the core functionality.

## Possible Future Upgrades

Here are some things not planned for the 1.0.0 release, but are ideas that could make the cut if there is interest.

- [ ] **Volunteer / Task Management**: Dashboard that features some task and volunteering scheduling information. Could use this to show a daily task list, or which volunteers are on today, etc.
- [ ] **Finances Management**: Transactions (tracking expenses/income) are expected to be available in v1.0.0.  Beyond that, reporting, sales, and tracking inventory are possible.
- [ ] **Multi-image and multi-doc uploads**: Not currently planned, but uploading things like x-rays and other images or docs could be added.
- [ ] **Robust permissions for Users**: The initial release will only have basic authentication, and all views will require the user to be logged in.  This may be expanded in the future to allow more granular access to viewing/editing/creating records based on group or role membership (Say, vet team role vs part-time volunteer role)
- [ ] **Widget-ized Dashboards**: What I mean by this - Dashboards that are "drag and drop" and allow you to easily customize what you see.  This will be a lot of work (I think) and won't be done unless there is an interest in it, or if I find a somewhat easy way of implementing it.
