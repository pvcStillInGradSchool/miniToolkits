# Usage:
#   ./pdf2svg.sh <input_dir>
for x in $(ls $1 | grep "pdf") ; do echo $x ; mutool convert -o ${x%.pdf}.svg $x ; done
for x in $(ls $1 | grep "1.svg") ; do mv $x ${x%1.svg}.svg ; done
