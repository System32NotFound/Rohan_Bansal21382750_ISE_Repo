require "cell"

class Grid
  attr_reader :rows, :columns
  attr_accessor :r, :g, :b

  def initialize(rows, columns)
    @rows = rows
    @columns = columns

    @r = 214
    @g = 220
    @b = 230

    @grid = prepare_grid
    configure_cells
  end

  def prepare_grid
    Array.new(rows) do |row|
      Array.new(columns) { |column| Cell.new(row, column) }
    end
  end

  def configure_cells
    each_cell do |cell|
      row, col = cell.row, cell.column

      cell.north = self[row - 1, col]
      cell.south = self[row + 1, col]
      cell.west = self[row, col - 1]
      cell.east = self[row, col + 1]
      cell.southeast = self[row + 1, col + 1]
    end
  end

  def [](row, column)
    return nil unless row.between?(0, @rows - 1)
    return nil unless column.between?(0, @grid[row].count - 1)
    @grid[row][column]
  end

  def random_cell
    row = rand(@rows)
    column = rand(@grid[row].count)

    self[row, column]
  end

  def size
    @rows * @columns
  end

  def each_row
    @grid.each { |row| yield row }
  end

  def each_cell
    each_row { |row| row.each { |cell| yield cell if cell } }
  end

  def contents_of(cell)
    " "
  end

  def background_color_for(cell)
    color = "\033[0m"
    color << black_foreground
    color
  end

  def reset_color
    color = "\033[0m"
    color << black_foreground
    color
  end

  def blend_colors(cell_one, cell_two)
    color = "\033[0m"
    color << black_foreground
    color
  end

  def black_foreground
    "\033[38;2;#{@r};#{@g};#{@b}m"
  end

  def to_s
    output = "+" + "-+" * columns + "\n"

    each_row do |row|
      top = "|"
      bottom = "+"

      row.each do |cell|
        cell = Cell.new(-1, -1) unless cell

        body = " "
        east_boundary = (cell.linked?(cell.east) ? " " : "|")
        top << body << east_boundary
        south_boundary = (cell.linked?(cell.south) ? " " : "-")
        corner = "+"
        bottom << south_boundary << corner
      end
      output << top << "\n"
      output << bottom << "\n"
    end

    output
  end
end
