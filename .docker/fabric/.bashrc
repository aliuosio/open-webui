export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$HOME/.local/bin:$PATH

alias pbpaste='xclip -selection clipboard -o'

for pattern_file in $HOME/.config/fabric/patterns/*; do
    pattern_name=$(basename "$pattern_file")
    alias_command="alias $pattern_name='fabric --pattern $pattern_name'"
    eval "$alias_command"
done

yt() {
    local video_link="$1"
    fabric -y "$video_link" --transcript
}