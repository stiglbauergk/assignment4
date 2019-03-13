# Create initial gamers

mongo KillCounter <<EOF

db.gamers.insert({name: "ninja_102", kills: [3,1,5]})
db.gamers.insert({name: "dangerman1212", grades: [8,4,7]})

EOF
