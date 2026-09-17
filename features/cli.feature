Feature: CLI output format

  Scenario: A JSON template is rendered as JSON
    Given a template file named "template.json"
      """
      {
        "Resources": {
          "Queue": {
            "Type": "AWS::SQS::Queue",
            "Properties": {"QueueName": {"Fn::Sub": "${AWS::Region}-queue"}}
          }
        }
      }
      """
    When I run the cfneval cli
    Then the cli output is "json"
    And the cli output contains "us-east-1-queue"

  Scenario: A YAML template is rendered as YAML
    Given a template file named "template.yaml"
      """
      Resources:
        Queue:
          Type: AWS::SQS::Queue
          Properties:
            QueueName: !Sub "${AWS::Region}-queue"
      """
    When I run the cfneval cli
    Then the cli output is "yaml"
    And the cli output contains "us-east-1-queue"
