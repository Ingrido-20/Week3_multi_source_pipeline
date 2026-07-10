import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Polygon, Group

def draw_header(c, title):
    # Background
    c.setFillColor(colors.HexColor('#0F172A'))  # Deep Slate Navy
    c.rect(0, 0, 792, 612, fill=True, stroke=False)
    
    # Header background strip
    c.setFillColor(colors.HexColor('#1E293B'))
    c.rect(0, 532, 792, 80, fill=True, stroke=False)
    
    # Accent bar
    c.setFillColor(colors.HexColor('#10B981'))  # Emerald Green
    c.rect(0, 529, 792, 3, fill=True, stroke=False)
    
    # Title Text
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 22)
    c.drawString(36, 558, title)
    
    # Logo / Course text
    c.setFont('Helvetica-Bold', 10)
    c.setFillColor(colors.HexColor('#94A3B8'))
    c.drawRightString(756, 574, "INUKA TECH DATA ANALYTICS")
    c.setFont('Helvetica', 9)
    c.drawRightString(756, 556, "Week 3 Assignment | Lightning Talk")

def draw_footer(c, page_num):
    # Divider line
    c.setStrokeColor(colors.HexColor('#334155'))
    c.setLineWidth(0.5)
    c.line(36, 45, 756, 45)
    
    # Footer text
    c.setFont('Helvetica', 8)
    c.setFillColor(colors.HexColor('#64748B'))
    c.drawString(36, 28, "Presenter: Ingrid Miriam | Email: miriamondu@gmail.com")
    c.drawRightString(756, 28, f"Slide {page_num} of 3")

def draw_slide_1(c):
    draw_header(c, "Optimizing Depot Performance")
    
    # Decorative elements - Slide 1 specific big title
    c.setFillColor(colors.HexColor('#0284C7'))  # Sky blue
    c.rect(36, 320, 10, 160, fill=True, stroke=False)
    
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 34)
    c.drawString(60, 430, "Why Did Operational Throughput Drop Last Week?")
    
    c.setFillColor(colors.HexColor('#E2E8F0'))
    c.setFont('Helvetica', 16)
    c.drawString(60, 395, "A Data-Driven Investigation into Mid-Year Flow Rate Fluctuations")
    
    c.setFillColor(colors.HexColor('#94A3B8'))
    c.setFont('Helvetica-Oblique', 11)
    c.drawString(60, 365, "Targeting Logistics, Weather, and Governance across Nairobi, Mombasa & Eldoret Terminals")
    
    # Highlights / Sub-text box
    c.setFillColor(colors.HexColor('#1E293B'))
    c.rect(36, 120, 720, 180, fill=True, stroke=False)
    
    # Accent for highlight box
    c.setFillColor(colors.HexColor('#38BDF8'))
    c.rect(36, 120, 3, 180, fill=True, stroke=False)
    
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 13)
    c.drawString(60, 270, "THE OPERATIONAL PROBLEM")
    
    c.setFillColor(colors.HexColor('#94A3B8'))
    c.setFont('Helvetica', 10.5)
    c.drawString(60, 248, "During the week of June 25 to July 1, 2026, the central operations console flagged a significant reduction")
    c.drawString(60, 230, "in mean flow rates (LPM) at several key depots, threatening daily distribution targets.")
    
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 12)
    c.drawString(60, 195, "Key Operational Questions Investigated:")
    
    c.setFont('Helvetica', 10.5)
    c.setFillColor(colors.HexColor('#CBD5E1'))
    c.drawString(80, 172, "- Environmental Impact: Did heavy precipitation trigger pump line friction or viscosity drops?")
    c.drawString(80, 154, "- Workforce Governance: Did team sizes or supervisor experience on the holiday night shift affect throughput?")
    c.drawString(80, 136, "- Machine Stability: Did localized pressure limits (100 - 300 PSI) remain within stable thresholds?")
    
    draw_footer(c, 1)
    c.showPage()

def draw_arrow(c, x1, y1, x2, y2):
    c.setStrokeColor(colors.HexColor('#38BDF8'))
    c.setLineWidth(1.5)
    c.line(x1, y1, x2, y2)
    # Draw arrow head
    if x2 > x1:
        c.setFillColor(colors.HexColor('#38BDF8'))
        p = c.beginPath()
        p.moveTo(x2, y2)
        p.lineTo(x2-6, y2+4)
        p.lineTo(x2-6, y2-4)
        p.close()
        c.drawPath(p, fill=True, stroke=False)
    elif y2 < y1:
        c.setFillColor(colors.HexColor('#38BDF8'))
        p = c.beginPath()
        p.moveTo(x2, y2)
        p.lineTo(x2-4, y2+6)
        p.lineTo(x2+4, y2+6)
        p.close()
        c.drawPath(p, fill=True, stroke=False)

def draw_slide_2(c):
    draw_header(c, "The Data Integration Architecture")
    
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 13)
    c.drawString(36, 490, "PIPELINE WORKFLOW: CSV + REST API + SQLITE DB")
    
    # Descriptions of sources
    c.setFont('Helvetica', 10)
    c.setFillColor(colors.HexColor('#94A3B8'))
    c.drawString(36, 472, "We developed a robust ETL pipeline merging three independent data sources into a standardized, date-aligned master hourly dataset.")
    
    # Draw boxes for data sources
    # 1. Cleaned CSV
    c.setFillColor(colors.HexColor('#1E293B'))
    c.rect(36, 310, 190, 120, fill=True, stroke=False)
    c.setFillColor(colors.HexColor('#F59E0B')) # Amber accent
    c.rect(36, 310, 190, 4, fill=True, stroke=False)
    
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 11)
    c.drawString(50, 410, "1. Internal CSV Source")
    c.setFont('Helvetica-Bold', 9)
    c.setFillColor(colors.HexColor('#CBD5E1'))
    c.drawString(50, 390, "File: ops_sensor_log_cleaned.csv")
    c.setFont('Helvetica', 9.5)
    c.setFillColor(colors.HexColor('#94A3B8'))
    c.drawString(50, 370, "- Pre-cleaned dataset")
    c.drawString(50, 353, "- Loaded directly in pandas")
    c.drawString(50, 336, "- Chronological sorting")
    c.drawString(50, 321, "- Hourly resampling")
    
    # 2. Weather REST API
    c.setFillColor(colors.HexColor('#1E293B'))
    c.rect(301, 310, 190, 120, fill=True, stroke=False)
    c.setFillColor(colors.HexColor('#06B6D4')) # Cyan accent
    c.rect(301, 310, 190, 4, fill=True, stroke=False)
    
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 11)
    c.drawString(315, 410, "2. External API Source")
    c.setFont('Helvetica-Bold', 9)
    c.setFillColor(colors.HexColor('#CBD5E1'))
    c.drawString(315, 390, "REST Endpoint: Open-Meteo API")
    c.setFont('Helvetica', 9.5)
    c.setFillColor(colors.HexColor('#94A3B8'))
    c.drawString(315, 370, "- Hourly Nairobi Weather")
    c.drawString(315, 353, "- Rain, Temp, Humidity")
    c.drawString(315, 336, "- Connection timeout handling")
    c.drawString(315, 321, "- Offline synthetic fallback")

    # 3. SQLite Database
    c.setFillColor(colors.HexColor('#1E293B'))
    c.rect(566, 310, 190, 120, fill=True, stroke=False)
    c.setFillColor(colors.HexColor('#10B981')) # Emerald accent
    c.rect(566, 310, 190, 4, fill=True, stroke=False)
    
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 11)
    c.drawString(580, 410, "3. Relational Database")
    c.setFont('Helvetica-Bold', 9)
    c.setFillColor(colors.HexColor('#CBD5E1'))
    c.drawString(580, 390, "Engine: SQLite via SQLAlchemy")
    c.setFont('Helvetica', 9.5)
    c.setFillColor(colors.HexColor('#94A3B8'))
    c.drawString(580, 370, "- holiday_calendar (Table)")
    c.drawString(580, 353, "- shift_details (Table)")
    c.drawString(580, 336, "- SQL JOIN and GROUP BY query")
    c.drawString(580, 321, "- Loaded via pd.read_sql")

    # Draw Integration / Merge Box
    c.setFillColor(colors.HexColor('#1E293B'))
    c.rect(200, 120, 392, 110, fill=True, stroke=False)
    c.setFillColor(colors.HexColor('#8B5CF6')) # Purple accent
    c.rect(200, 120, 392, 4, fill=True, stroke=False)
    
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 12)
    c.drawString(220, 205, "Unified Date-Aligned Master DataFrame")
    c.setFont('Helvetica', 9.5)
    c.setFillColor(colors.HexColor('#CBD5E1'))
    c.drawString(220, 185, "- Operational logs resampled to hourly means by Zone & Shift")
    c.drawString(220, 168, "- Merged with Weather on timestamp (Many-to-One)")
    c.drawString(220, 151, "- Merged with SQLite on Date, Zone, and Shift (Many-to-One)")
    c.drawString(220, 134, "- Missing values resolved using linear ffill() and bfill()")
    
    # Draw Arrows
    draw_arrow(c, 131, 310, 131, 260)
    draw_arrow(c, 396, 310, 396, 260)
    draw_arrow(c, 661, 310, 661, 260)
    
    # Connect outer arrows to merge box
    c.setStrokeColor(colors.HexColor('#38BDF8'))
    c.setLineWidth(1.5)
    c.line(131, 260, 250, 260)
    draw_arrow(c, 250, 260, 250, 230)
    
    c.line(661, 260, 542, 260)
    draw_arrow(c, 542, 260, 542, 230)
    
    draw_arrow(c, 396, 260, 396, 230)

    draw_footer(c, 2)
    c.showPage()

def draw_slide_3(c):
    draw_header(c, "Insights & Strategic Recommendations")
    
    # Create 3 columns for insights
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 13)
    c.drawString(36, 490, "KEY FINDINGS FROM MULTI-SOURCE ANALYSIS")
    
    # Column 1: The Weather Myth
    c.setFillColor(colors.HexColor('#1E293B'))
    c.rect(36, 120, 226, 340, fill=True, stroke=False)
    c.setFillColor(colors.HexColor('#3B82F6')) # Blue accent
    c.rect(36, 456, 226, 4, fill=True, stroke=False)
    
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 11)
    c.drawString(50, 435, "1. The Weather Myth")
    c.setFont('Helvetica-Oblique', 9)
    c.setFillColor(colors.HexColor('#38BDF8'))
    c.drawString(50, 420, "Statistical Correlation r = 0.00")
    c.setFont('Helvetica', 9.5)
    c.setFillColor(colors.HexColor('#CBD5E1'))
    # Draw wrapped text
    c.drawString(50, 395, "Our Pearson correlation matrix")
    c.drawString(50, 380, "shows that rainfall has exactly")
    c.drawString(50, 365, "r = 0.00 correlation with")
    c.drawString(50, 350, "mean flow rates.")
    c.drawString(50, 325, "Insight:")
    c.setFillColor(colors.HexColor('#94A3B8'))
    c.drawString(50, 310, "Depot pumps and lines are")
    c.drawString(50, 295, "physically shielded, meaning")
    c.drawString(50, 280, "precipitation does NOT directly")
    c.drawString(50, 265, "retard pipe hydraulics.")

    # Column 2: Shift Capacity Bottleneck
    c.setFillColor(colors.HexColor('#1E293B'))
    c.rect(283, 120, 226, 340, fill=True, stroke=False)
    c.setFillColor(colors.HexColor('#EF4444')) # Red accent
    c.rect(283, 456, 226, 4, fill=True, stroke=False)
    
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 11)
    c.drawString(297, 435, "2. Governance & Staffing")
    c.setFont('Helvetica-Oblique', 9)
    c.setFillColor(colors.HexColor('#F87171'))
    c.drawString(297, 420, "Night Shift Capacity Cut by 50%")
    c.setFont('Helvetica', 9.5)
    c.setFillColor(colors.HexColor('#CBD5E1'))
    c.drawString(297, 395, "Night shifts operate with a")
    c.drawString(297, 380, "planned team size of 4, compared")
    c.drawString(297, 365, "to 8 on Morning shifts.")
    c.drawString(297, 340, "Insight:")
    c.setFillColor(colors.HexColor('#94A3B8'))
    c.drawString(297, 325, "On holidays and rainy nights,")
    c.drawString(297, 310, "this capacity drop leads to")
    c.drawString(297, 295, "delayed maintenance recovery,")
    c.drawString(297, 280, "resulting in prolonged system")
    c.drawString(297, 265, "throttling.")

    # Column 3: Recommendations
    c.setFillColor(colors.HexColor('#1E293B'))
    c.rect(530, 120, 226, 340, fill=True, stroke=False)
    c.setFillColor(colors.HexColor('#10B981')) # Emerald accent
    c.rect(530, 456, 226, 4, fill=True, stroke=False)
    
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 11)
    c.drawString(544, 435, "3. Actionable Strategy")
    c.setFont('Helvetica-Oblique', 9)
    c.setFillColor(colors.HexColor('#34D399'))
    c.drawString(544, 420, "Director Recommendations")
    c.setFont('Helvetica', 9.5)
    c.setFillColor(colors.HexColor('#CBD5E1'))
    c.drawString(544, 395, "Operational changes to make:")
    
    c.drawString(544, 370, "1. Weather-Adaptive Staffing:")
    c.setFillColor(colors.HexColor('#94A3B8'))
    c.drawString(544, 355, "Increase holiday night shifts")
    c.drawString(544, 340, "from 4 to 6 when storm warnings")
    c.drawString(544, 325, "are active.")
    
    c.setFillColor(colors.HexColor('#CBD5E1'))
    c.drawString(544, 300, "2. Supervisor Reallocation:")
    c.setFillColor(colors.HexColor('#94A3B8'))
    c.drawString(544, 285, "Assign top performing leads")
    c.drawString(544, 270, "(Munyao, Njoroge) to holiday")
    c.drawString(544, 255, "night shifts during wet seasons.")

    draw_footer(c, 3)
    c.showPage()

def generate_pdf(filename):
    c = canvas.Canvas(filename, pagesize=landscape(letter))
    draw_slide_1(c)
    draw_slide_2(c)
    draw_slide_3(c)
    c.save()
    print(f"PDF presentation saved to {filename}")

if __name__ == '__main__':
    generate_pdf("Week3_LightningTalk_Slides.pdf")
    generate_pdf("Week3_LightningTalk_IngridMiriam_Slides.pdf")
