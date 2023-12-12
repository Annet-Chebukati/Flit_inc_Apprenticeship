# Data Management in SQL

This repository documents the process of managing hotel reservation data using SQL and integrating it with Tableau for analysis. The process is divided into several key stages, as outlined below.

## Database Environment

Utilizing **PostgreSQL 16** and the intuitive interface of **pgAdmin4**, I imported the prepared dataset into a structured SQL environment. This setup provided a robust platform for handling complex data operations and queries.

## Schema Design

I crafted a schema that mirrors the complexities of hotel operations. The schema encompasses tables for:

- Reservations
- Market Segments
- Distribution Channels
- Meals

Each table was designed with relational integrity in mind, complete with primary and foreign keys to ensure data consistency and facilitate complex queries.

## Data Transformation

The SQL queries were used to organize the data effectively. The following steps were taken to transform the data:

1. Executed SQL queries within PostgreSQL to organize and prepare the data for export.
2. Transformed the data into a CSV file format directly within the PostgreSQL environment.
3. Download the CSV files for further analysis in  **Tableau Public**.

## Integration with Tableau

The downloaded CSV file was then converted into Excel files, namely `HotelReservationData` and `Dimension Tables`. These files were uploaded to Tableau, allowing for comprehensive data analysis through visualizations and [dashboard](https://public.tableau.com/views/Hotel_Reservation_Analysis/Dashboard?:language=en-US&:display_count=n&:origin=viz_share_link).

---

The repository includes all SQL scripts and Excel documents used in this process. Feel free to explore the data and the corresponding Tableau dashboard for a deeper understanding of hotel reservation patterns and trends.
