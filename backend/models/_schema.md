USER
- login info

PIECE
- author
- Title
- Selected title ID
- Selected Version ID
- Info: text field
- Info time last modified

PIECE TAGS
- Piece Id
- Tag Id

// make tables for collections, statuses etc

TAGS
- TagID
- Tag type
- Tag value
 
FAVORITES
- Version ID
- User ID

TITLES
- Title ID
- Piece ID
- text: varchar

VERSION
 - height
 - width

FILES (base class)
- Piece ID
- upload_name
- name
- Storage_ID
- mimetype

PHOTOS
- Photo ID
- Piece ID
- created
- deleted
- metadata

PROJECT_FILES
- Project File ID
- Piece ID
- date uploaded

PIECE_USER_ACESS
- User ID
- Piece ID

USER_TO_USER_CONNECTIONS
- User ID
- User ID