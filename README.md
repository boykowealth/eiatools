# EIATools Python Package
_EIATools is a collaberative project aimed at making the EIA APIv2 accessible to developers. The project spans across Python and R, with a desktop application available through Dockerhub. The project is maintained by Justin Powley and Brayden Boyko._

---
+ [View The R Package](https://github.com/jspowley/eiatools)
+ [View The Desktop App](https://hub.docker.com/r/jspowley/eiatools_shiny)
---
## Repository Structure
+ build_index.py – Constructs an index for organizing and retrieving EIA data efficiently.
+ collapse_index.py – Merges and optimizes index structures to reduce redundancy and improve data lookup performance.
+ data_tree.py – Builds hierarchical representations of EIA datasets to facilitate navigation and querying.
+ detect_routes.py – Identifies and maps available API routes for accessing various EIA datasets.
+ dindex_get_data.py – Retrieves indexed data based on predefined structures and parameters.
+ eia_call.py – Handles API requests and responses for retrieving data from the EIA API.
+ eia_data.py – Core module for processing, cleaning, and structuring retrieved EIA data.
+ eia_map.py – Generates mappings between API endpoints, metadata, and user-friendly dataset descriptions.
+ eia_meta.py – Fetches and processes metadata for various datasets, including descriptions, sources, and update frequencies.
+ eia_version.py – Tracks and manages API versioning for compatibility with updates and changes.
+ get_all_data_types.py – Retrieves and lists all available data types from the EIA API.
+ get_all_freq.py – Queries available data frequencies (e.g., hourly, daily, monthly) and organizes them for selection.
+ get_facet_data.py – Extracts specific data facets for detailed analysis and filtering.
+ get_facet_types.py – Identifies and categorizes facet types for more granular data queries.
+ get_routes.py – Fetches and organizes API route information for streamlined data access.
+ internal_data.py – Manages internal caching and storage of frequently accessed data.
+ map_headers.py – Aligns API response headers with predefined schema mappings for consistency.
+ route_tree.py – Constructs a structured representation of API routes for easier reference and usage.

## Installation

To install the EIATools package, follow these steps:

Clone the repository:

git clone https://github.com/boykowealth/eiatools.git
cd eiatools

Install dependencies and the package:

pip install -r requirements.txt
python setup.py install

## Usage

After installation, you can import and use the package modules to interact with the EIA API. Example usage and documentation will be added in future updates.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the GPL-3.0 License. See the LICENSE file for details.

 
