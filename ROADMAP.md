# Roadmap

The full span of functionality that Dragonroost will eventually encompass.

## Modules

These are the core application modules that will be available on the 1.0.0 release.

- [ ] **Animals**: The core module - management of animals and their related information.
- [ ] **People**: Management of volunteers, donors, fosters, and adopters.
- [ ] **Business**: Location management, donation tracking, and more.
- [ ] **Medical**: Reporting, vaccine calendar, and more.


Each module will have the following general functionality:

- [ ] **Add / Edit / Deletion**: Easy management of animals, people, etc.
- [ ] **Homepage Dashboard**: Each module will have a dashboard with different metrics and information.
- [ ] **Filterable, sortable searching**: Each data type will have a robust search table for easy location of individual records.

Some site-wide features that are planned for 1.0.0

- [ ] **Notifications**: The scope of these is not decided yet - but will likely include intake/outcome notifs. App only.
- [ ] **Reminders**: For vaccines, treatments, perhaps donation follow-ups, and more. Email, app, and mobile.

## Animal Module

The animal module will feature the following items:

- [X] **Animal records**
- [X] **Species records**
- [ ] **Medical records**: These are specifically tied to individual animals.
- [ ] **Dashboard**: With intake/outcome stats, counts for animals, and more.

## Business Module

The business module will feature the following items:

- [X] **Location management**: Can be separate buildings, or things like "quarantine room". This is just to help keep track of which animals are where.
- [ ] **Donation tracking**: Can optionally be linked to a person in the People module, or tracked separately.

## People Module

The people module will feature the following items:

- [ ] **People Management**: Not to be confused with Users of the application.  People include volunteers, adopters, fosters, donors, partners, etc.

## Medical Module

The medical module will feature the following items:

- [ ] **Vaccine dashboard**: Using the information from the animals' medical records to generate the calendar.

## In What Order Will This Be Done?

The animal module is going to be the core of the app, and will be fleshed out first.  That said, some portions of the other modules are already in place and required - for example, animals need to have a location so that is online already. The core records are first, with the dashboards coming later.

## Possible Future Upgrades

Here are some things not planned for the 1.0.0 release, but are ideas that could make the cut if there is interest.

- [ ] **Volunteer / Task Management**: Dashboard that features some task and volunteering scheduling information. Could use this to show a daily task list, or which volunteers are on today, etc.
- [ ] **Finances Management**: 1.0.0 will feature a very basic donations or income tracking feature.  A more comprehensive financial management section could be added to the business module. For example, tracking sales of merch, supplies - and more useful reporting.
- [ ] **Multi-image and multi-doc uploads**: Not currently planned, but uploading things like x-rays and other images or docs could be added.
- [ ] **Robust permissions for Users**: The initial release will only have basic authentication, and all views will require the user to be logged in.  This may be expanded in the future to allow more granular access to viewing/editing/creating records based on group or role membership (Say, vet team role vs part-time volunteer role)
- [ ] **Widget-ized Dashboards**: What I mean by this - Dashboards that are "drag and drop" and allow you to easily customize what you see.  This will be a lot of work (I think) and won't be done unless there is an interest in it, or if I find a somewhat easy way of implementing them.