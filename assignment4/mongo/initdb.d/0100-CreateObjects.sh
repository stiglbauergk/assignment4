# Create a database and collection for gamer details

mongo <<EOF

use KillCounter

db.createCollection("gamers")

EOF
