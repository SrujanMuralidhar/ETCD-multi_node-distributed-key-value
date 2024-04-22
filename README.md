# Etcd Multi-Node Distributed Key-Value Store

## Overview

This project aims to create a distributed key-value store using etcd, a distributed reliable key-value store for the most critical data of a distributed system.

### Files Structure

- `app.py`: Frontend application built using Streamlit.
- `client.py`: Main logic for interacting with the etcd cluster.
- `etcd.config.yml`: Configuration files for multiple etcd nodes.

## Installation

### Etcd 
To install etcd, use the following command:

```bash
sudo apt install etcd
```

### Streamlit

To install Streamlit, use the following command:

```bash
pip install streamlit
```

### etcd-python

To install the etcd-python library, you can use pip:

```bash
pip install etcd-python
```

## Running the Application

1. **Start etcd Cluster**: Before running the application, make sure to have multiple etcd nodes running. You can use the provided `etcd.config.yml` files to configure each node.

   To start an etcd node using a configuration file, use the following command:

   ```bash
   etcd --config-file <path_to_config_file>
   ```

2. **Run the Frontend**: Start the frontend application by running `app.py`:

   ```bash
   streamlit run app.py
   ```

3. **Interacting with the Cluster**: The `client.py` file contains the logic for interacting with the etcd cluster. You can import this file into your project and use its functions to perform operations on the etcd key-value store.

## Usage

1. **Frontend**: Access the frontend application by opening the provided URL after running `app.py`. Use the interface to interact with the key-value store.

2. **Backend Logic**: If you need to perform operations programmatically, import the `client.py` file into your project and use its functions to interact with the etcd cluster.

