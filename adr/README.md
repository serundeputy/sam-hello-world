# Scenario - Architectural Decision Record (ADR)

## Context
Some apps have been using a third party package and installing it directly from a tar file hosted on the third party company's website.

e.g. http://third-party.domain.com/packages/package_1.0.1.tar.gz

Their recommendation is to keep the package updated at least every three months.

We want an automated solution that allows apps to keep their package version updated to the latest release. We also want to host the tar file on our own S3 bucket.

We know the third party company has an RSS feed with an XML file for new releases.  The XML file contains data for:
- the link to the package
- the new package version
- the description and
- the release date

Please use the `000-template.md` template to write an ADR that explains your approach to this scenario.

We are looking for a clear explanation on how you would approach this, what the benefits and drawbacks are, and what other considerations you would make.