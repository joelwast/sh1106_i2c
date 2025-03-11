from machine import Pin, I2C
import framebuf

# Definiciones de comandos SH1106
SH1106_I2C_ADDRESS = 0x3C  # Dirección I2C del SH1106
SH1106_SETCONTRAST = 0x81
SH1106_DISPLAYALLON_RESUME = 0xA4
SH1106_DISPLAYALLON = 0xA5
SH1106_NORMALDISPLAY = 0xA6
SH1106_INVERTDISPLAY = 0xA7
SH1106_DISPLAYOFF = 0xAE
SH1106_DISPLAYON = 0xAF
SH1106_SETDISPLAYOFFSET = 0xD3
SH1106_SETCOMPINS = 0xDA
SH1106_SETVCOMDETECT = 0xDB
SH1106_SETDISPLAYCLOCKDIV = 0xD5
SH1106_SETPRECHARGE = 0xD9
SH1106_SETMULTIPLEX = 0xA8
SH1106_SETLOWCOLUMN = 0x00
SH1106_SETHIGHCOLUMN = 0x10
SH1106_SETSTARTLINE = 0x40
SH1106_MEMORYMODE = 0x20
SH1106_COLUMNADDR = 0x21
SH1106_PAGEADDR = 0x22
SH1106_COMSCANINC = 0xC0
SH1106_COMSCANDEC = 0xC8
SH1106_SEGREMAP = 0xA0
SH1106_CHARGEPUMP = 0x8D
SH1106_EXTERNALVCC = 0x1
SH1106_SWITCHCAPVCC = 0x2

# Tamaño de la pantalla
SH1106_LCDWIDTH = 128
SH1106_LCDHEIGHT = 64

class SH1106_I2C:
    def __init__(self, i2c, addr=SH1106_I2C_ADDRESS):
        self.i2c = i2c
        self.addr = addr
        self.width = SH1106_LCDWIDTH
        self.height = SH1106_LCDHEIGHT
        self.buffer = bytearray(self.height * self.width // 8)
        self.framebuf = framebuf.FrameBuffer(self.buffer, self.width, self.height, framebuf.MONO_VLSB)
        self.init_display()

    def init_display(self):
        self.write_cmd(SH1106_DISPLAYOFF)
        self.write_cmd(SH1106_SETDISPLAYCLOCKDIV)
        self.write_cmd(0x80)
        self.write_cmd(SH1106_SETMULTIPLEX)
        self.write_cmd(0x3F)
        self.write_cmd(SH1106_SETDISPLAYOFFSET)
        self.write_cmd(0x00)
        self.write_cmd(SH1106_SETSTARTLINE | 0x00)
        self.write_cmd(SH1106_CHARGEPUMP)
        self.write_cmd(0x14)
        self.write_cmd(SH1106_MEMORYMODE)
        self.write_cmd(0x00)
        self.write_cmd(SH1106_SEGREMAP | 0x1)
        self.write_cmd(SH1106_COMSCANDEC)
        self.write_cmd(SH1106_SETCOMPINS)
        self.write_cmd(0x12)
        self.write_cmd(SH1106_SETCONTRAST)
        self.write_cmd(0xCF)
        self.write_cmd(SH1106_SETPRECHARGE)
        self.write_cmd(0xF1)
        self.write_cmd(SH1106_SETVCOMDETECT)
        self.write_cmd(0x40)
        self.write_cmd(SH1106_DISPLAYALLON_RESUME)
        self.write_cmd(SH1106_NORMALDISPLAY)
        self.write_cmd(SH1106_DISPLAYON)

    def write_cmd(self, cmd):
        self.i2c.writeto(self.addr, bytearray([0x80, cmd]))

    def write_data(self, buf):
        self.i2c.writeto(self.addr, b'\x40' + buf)

    def show(self):
        for page in range(8):
            self.write_cmd(0xB0 + page)
            self.write_cmd(0x02)
            self.write_cmd(0x10)
            self.write_data(self.buffer[page * 128:(page + 1) * 128])

    def fill(self, color):
        self.framebuf.fill(color)

    def pixel(self, x, y, color):
        self.framebuf.pixel(x, y, color)

    def text(self, string, x, y, color=1):
        self.framebuf.text(string, x, y, color)