# Raritan server reciever
Simple server to allow connection from Raritan PDU to test the PDU's ability to push data using the Data Push function of these devices.

## Process
Steps required to test the Raritan PDU unit:
1. Connect to the Raritan PDU using web UI
2. Create a key pair on the local device
3. Create a DataPush configuration on the PDU using the generated key pair
4. Configure the payload on the side of the PDU
5. Trigger DataPush
6. Check if the payload arrived on the local device
