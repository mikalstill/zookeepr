# File for holding configuration relative to the current LCA
# This could be dberised sometimes
from datetime import datetime
import os


lca_info = {
  'paymentgateway_userid' : '',
  'paymentgateway_secretkey' : '',

# Contact email for the committee
  'contact_email' : 'contact@lca2013.linux.org.au',
# All email sent by ZK will Bcc here:
  'bcc_email' : 'archive@lca2013.linux.org.au',
  'webmaster_email': 'webmaster@lca2013.linux.org.au',

# Event information
  'event_parent_organisation' : 'Linux Australia',
  'event_parent_url' : 'http://www.linux.org.au/',
  'event_name' : 'linux.conf.au 2013',
  'event_shortname' : 'lca2013',
  'event_host' : 'lca2013.linux.org.au',
  'event_url' : 'http://lca2013.linux.org.au',
  'event_permalink' : 'http://lca2013.linux.org.au',
  'event_hashtag' : '#LCA2013',
  'event_tax_number' : 'ABN 56 987 117 479',
  'event_postal_address' : 'PO BOX 530, Woden, ACT, 2606',
  'event_fax_number' : '',
  'event_phone_number': '+61 2 6140 4546',
  'event_byline': 'linux.conf.au 2013 | 28 Jan - 1 Feb | Come Join the Party',
  'event_pricing_disclaimer': 'All prices are in Australian dollars and include 10% GST.',
  'date' : datetime(2011, 1, 28, 9, 0, 00),
  'media_license_name' : 'Creative Commons Attribution-Share Alike License',
  'media_license_url'  : 'http://creativecommons.org/licenses/by-sa/3.0/',
  #'sales_tax_multiplier' : 0.125,
  'sales_tax_divisor'    : 11,

  'invoice_message' : 'To qualify for the earlybird discount you must have registered and paid by the 8th of November (unless earlybird tickets sell out earlier).',

# Possible statuses not_open|open|closed
  'cfp_status' : 'open',
  'cfmini_status' : 'open',
  'paper_editing' : 'open',
  'funding_status' : 'not_open',
  'funding_editing' : 'not_open',
  'conference_status': 'not_open',
  'account_creation': True,
# Mode
  'cfp_hide_assistance_info': 'no',
  'cfp_hide_assistance_options': 'no',
  'cfp_hide_scores': 'no',

  'cfp_miniconf_list' : ["(none)", "Sysadmin", "Business", "Haecksen"],

  'emails': {
     'presentation' : 'speakers@lca2013.linux.org.au',
     'tutorial - 1 hour and 30 minutes'     : 'speakers@lca2013.linux.org.au',
     'miniconf'     : 'miniconfs@lca2013.linux.org.au',
     'funding'      : 'funding@lca2013.linux.org.au',
  },

  'proposal_update_email': 'archive@lca2013.linux.org.au', # recieve notifications when proposals are changed. Leave blank for none.

  'google_map_url': 'https://maps.google.com/maps/ms?ie=UTF8&hl=en&msa=0&msid=117014168848232117270.00048b169407c904d6506',
  'google_map_latlng': '-35.308056,149.124444',
}

lca_rego = {
  'personal_info' : {
      'phone' : 'yes',
      'home_address' : 'yes',
  },

  # Set to yes to collect PGP key IDs in rego, no to disable collection.
  'pgp_collection': 'yes',

  # Set to no once the conference starts to speed things up
  'confirm_email_address' : 'yes',

  'volunteer':
    (
        {'title': 'Volunteer Category', 'questions':
            (
                {'name': 'Student Volunteer', 'description': 'I am eligible to attend as a Student and am willing to donate 100% of my time to the conference. I understand that I will be able to attend for free.'},
                {'name': 'Hobbyist Volunteer', 'description': 'I am eligible to attend as a Hobbyist and am willing to donate at least 50% of my time to the conference. I understand that I will be able to attend for the price of a student admission. (If you are happy to donate more than 50% of your time, please indicate a percentage in the "Other:" section.)'},
                {'name': 'Other Volunteer', 'description': 'I do not fit into the categories above or want to volunteer for a specific project or for less than the percentages above. Please provide details in the "Other:" section.'},
            )
        },
        {'title': 'Availability', 'questions':
            (
                {'name': 'Setup', 'description': 'I am available on the weekend prior to the conference (22 - 23 January) to help with setup.'},
                {'name': 'Sunday Registrations', 'description': 'I am available on the afternoon of Sunday 23 January to assist with pre-conference registrations.'},
                {'name': 'Conference', 'description': 'I am available for the full week of the conference (24 - 28 January).'},
                {'name': 'Pack up', 'description': 'I am available on the evening of Friday 28 January and Saturday 29 January to pack-up the conference.'},
                {'name': 'Other Dates', 'description': 'Please provide details in the "Other:" section.'},
            )
        },
        {'title': 'I am able and willing to help with ...', 'questions':
            (
                {'name': 'Speaker Introductions', 'description': 'Leading A/V and Ushers in a room, introducing speakers, keeping them to schedule, public announcements, etc.'},
                {'name': 'A/V', 'description': 'Filming in a lecture theatre. Training will be provided.'},
                {'name': 'Usher', 'description': 'Helping manage rooms, get people to seats, etc.'},
                {'name': 'Registration Desk', 'description': 'Sign people into the conference and help with general enquiries.'},
                {'name': 'Venue Helper', 'description': 'Help with setting up break times, tables and chairs, and other miscellaneous things.'},
                {'name': 'Other', 'description': 'Please provide details in the "Other:" section.'},
            ),
        }
    ),
  'shells' : ['bash', 'busybox', 'csh', 'dash', 'emacs', 'ksh', 'sh', 'smrsh', 'tcsh', 'XTree Gold', 'zsh'],
  'editors' : ['bluefish', 'eclipse', 'emacs', 'gedit', 'jed', 'kate', 'nano', 'vi', 'vim', 'xemacs'],
  'distros' : ['Arch', 'Arch/Hurd', 'CentOS', 'Darwin', 'Debian', 'Fedora', 'FreeBSD', 'FreeDOS', 'Gentoo', 'Hurd', 'GNU Emacs','Haiku OS','kFreeBSD','L4', 'Mandriva', 'Minix', 'MeeGo', 'NetBSD', 'Nexenta', 'OpenBSD', 'OpenSolaris', 'OpenSuSE', 'SLES','Oracle Enterprise Linux', 'RHEL', 'Slackware', 'Ubuntu', 'Xandros'],
  'vcses' : ['.bak', 'arch', 'bazaar', 'bitkeeper', 'cvs', 'darcs', 'git', 'mercurial', 'monotone', 'perforce', 'rcs', 'sourcesafe', 'subversion'],
  'past_confs' : [('99', '1999 (CALU, Melbourne)'), ('01', '2001 (Sydney)'), ('02', '2002 (Brisbane)'), ('03', '2003 (Perth)'), ('04', '2004 (Adelaide)'), ('05', '2005 (Canberra)'), ('06', '2006 (Dunedin)'), ('07', '2007 (Sydney)'), ('08', '2008 (Melbourne)'), ('09', '2009 (Hobart)'), ('10', '2010 (Wellington)')],

  'silly_description' : {
        'starts' : ["a", "a", "a", "one", "no"], # bias toward "a"
        'adverbs' : ["strongly",
               "poorly", "badly", "well", "dynamically",
               "hastily", "statically", "mysteriously",
               "buggily", "extremely", "nicely", "strangely",
               "irritatingly", "unquestionably", "clearly",
               "plainly", "silently", "abstractly", "validly",
               "invalidly", "immutably", "oddly", "disturbingly",
               "atonally", "randomly", "amusingly", "widely",
               "narrowly", "manually", "automatically", "audibly",
               "brilliantly", "independently", "definitively",
               "provably", "improbably", "distortingly",
               "confusingly", "decidedly", "historically",
               "shiny", "troublesome"],
        'adjectives' : ["invalid", "valid",
               "referenced", "dereferenced", "unreferenced",
               "illegal", "legal",
               "questionable",
               "alternate", "implemented", "unimplemented",
               "terminal", "non-terminal",
               "static", "dynamic",
               "qualified", "unqualified",
               "constant", "variable",
               "volatile", "non-volatile",
               "abstract", "concrete",
               "fungible", "non-fungible",
               "untyped", "variable",
               "mutable", "immutable",
               "sizable", "minuscule",
               "perverse", "immovable",
               "compressed", "uncompressed",
               "surreal", "allegorical",
               "trivial", "nontrivial"],
        'nouns' : ["pointer", "structure",
               "definition", "declaration", "type", "union",
               "coder", "admin", "hacker", "kitten", "mistake",
               "conversion", "implementation", "design", "analysis",
               "neophyte", "expert", "bundle", "package",
               "abstraction", "theorem", "display", "distro",
               "restriction", "device", "function", "reference",
               "alien"]
    }
}

lca_menu = [
 ('Home', '/', 'home'),
 ('About', '/about/linux.conf.au', 'about'),
 ('Call for Proposals', '/cfp', 'cfp'),
 ('Call for Miniconfs', '/miniconf-cfp', 'miniconf-cfp'),
 ('FAQ', '/faq', 'faq'),
 ('Conditions of Registration', '/cor/terms_and_conditions', 'cor'),
 ('Contact', '/contact', 'contact'),
]

lca_submenus = {
 'about': ['linux.conf.au', 'Venues', 'Transport', '2013 Team'],
 'cor': ['Terms and Conditions', 'Code Of Conduct'],
}
